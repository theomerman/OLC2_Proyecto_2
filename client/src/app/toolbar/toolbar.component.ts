import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SetTextService } from '../services/setText/set-text.service';

@Component({
  selector: 'app-toolbar',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './toolbar.component.html',
  styleUrl: './toolbar.component.css'
})
export class ToolbarComponent {
  fileContent: string = '';

  constructor(private sendText: SetTextService) { }
  setText(event: any): void {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = () => {
      this.fileContent = reader.result as string;
      this.send(this.fileContent);
    };
    reader.readAsText(file);
  }
  send(text: string): void{
    this.sendText.sendString(text);
  }
}
