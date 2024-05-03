import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { SetTextService } from '../services/setText/set-text.service';
import { SendToServerService } from '../services/sendToServer/send-to-server.service';

@Component({
  selector: 'app-editor',
  standalone: true,
  imports: [FormsModule, MonacoEditorModule],
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.css'
})
export class EditorComponent {
  editorOptions = { theme: 'vs-dark', language: 'typescript' };
  code: string = '';
  constructor(private reveivedData: SetTextService, private sendToServer: SendToServerService) {
    this.reveivedData.string$.subscribe(data => {
      this.code = data;
    });
  }
  sendCode(): void {
    this.sendToServer.sendCode({ "code": this.code }).subscribe(
      (response: any) => {

        this.sendToServer.object = response;
        console.log(response);
        var tmp = response['console'];
        this.sendToServer.variableSubject.next(tmp);
      },
      error => {
        console.log(error);
        // alert('There was an error sending your message' + error);
      });


  }

}
