import * as vscode from 'vscode';

class CommentItem extends vscode.TreeItem {
    constructor(
        public readonly label: string,
        public readonly collapsibleState: vscode.TreeItemCollapsibleState,
        public readonly filePath?: string,
        public readonly lineNumber?: number
    ) {
        super(label, collapsibleState);
        if (filePath && lineNumber !== undefined) {
            this.command = {
                command: 'extension.comment-organizer.goToComment',
                title: 'Перейти к комментарию',
                arguments: [{ file: filePath, line: lineNumber }]
            };
        }
    }
}

class CommentTreeDataProvider implements vscode.TreeDataProvider<CommentItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<CommentItem | undefined | void> = new vscode.EventEmitter();
    readonly onDidChangeTreeData: vscode.Event<CommentItem | undefined | void> = this._onDidChangeTreeData.event;

    private comments: { file: string; line: number; text: string }[] = [];

    refresh(newComments: { file: string; line: number; text: string }[]): void {
        this.comments = newComments;
        this._onDidChangeTreeData.fire();
    }

    getChildren(element?: CommentItem): CommentItem[] {
        if (!element) {
            const files = Array.from(new Set(this.comments.map(comment => comment.file)));
            return files.map(file => new CommentItem(file, vscode.TreeItemCollapsibleState.Collapsed));
        } else {
            return this.comments
                .filter(comment => comment.file === element.label)
                .map(comment =>
                    new CommentItem(
                        `Comment: ${comment.text}`,
                        vscode.TreeItemCollapsibleState.None,
                        comment.file,
                        comment.line
                    )
                );
        }
    }

    getTreeItem(element: CommentItem): vscode.TreeItem {
        return element;
    }
}

export function activate(context: vscode.ExtensionContext) {
    const commentProvider = new CommentTreeDataProvider();
    vscode.window.createTreeView('commentView', { treeDataProvider: commentProvider });

    context.subscriptions.push(
        vscode.commands.registerCommand('extension.comment-organizer.refresh', async () => {
            const files = await vscode.workspace.findFiles('**/*.{cpp,h,hpp,c,ts,js}');
            const allComments = [];

            for (const file of files) {
                const document = await vscode.workspace.openTextDocument(file);
                const comments = findCommentsInDocument(document).map(comment => ({
                    file: file.fsPath,
                    ...comment
                }));
                allComments.push(...comments);
            }

            commentProvider.refresh(allComments);
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('extension.comment-organizer.goToComment', async ({ file, line }) => {
            const uri = vscode.Uri.file(file);
            const editor = await vscode.window.showTextDocument(uri);
            const position = new vscode.Position(line - 1, 0);
            editor.revealRange(new vscode.Range(position, position));

            const deleteOption = await vscode.window.showQuickPick(['Delete this comment', 'Cancel'], {
                placeHolder: 'What would you like to do?'
            });

            if (deleteOption === 'Delete this comment') {
                const edit = new vscode.WorkspaceEdit();
                edit.delete(uri, new vscode.Range(position, position.translate(0, editor.document.lineAt(line - 1).text.length)));
                await vscode.workspace.applyEdit(edit);
            } 
        })
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('extension.comment-organizer.deleteAllComments', async () => {
            const files = await vscode.workspace.findFiles('**/*.{cpp,h,hpp,c,ts,js}');
            const edit = new vscode.WorkspaceEdit();

            for (const file of files) {
                const document = await vscode.workspace.openTextDocument(file);
                const comments = findCommentsInDocument(document);

                for (const comment of comments) {
                    const start = new vscode.Position(comment.line - 1, comment.pos);
                    const end = new vscode.Position(comment.line - 1, comment.pos + document.lineAt(comment.line - 1).text.length + 1);
                    edit.delete(document.uri, new vscode.Range(start, end));
                }
            }

            await vscode.workspace.applyEdit(edit);
            vscode.window.showInformationMessage('All comments have been deleted.');
        })
    );
}

export function findCommentsInDocument(document: vscode.TextDocument): { line: number; text: string, pos: number}[] {
    const regex = /(\/\/.*|\/\*[\s\S]*?\*\/)/g;
    const text = document.getText();
    const comments = [];
    let match;
	const commentStartPattern = /\/\//;
    while ((match = regex.exec(text)) !== null) {
        comments.push({
            line: document.positionAt(match.index).line + 1,
			pos: document.positionAt(match.index).character, 
            text: match[1].trim()
        });
    }

    return comments;
}

export function deactivate() {}
