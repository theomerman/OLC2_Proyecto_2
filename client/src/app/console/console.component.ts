import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SendToServerService } from '../services/sendToServer/send-to-server.service';

@Component({
  selector: 'app-console',
  standalone: true,
  imports: [],
  templateUrl: './console.component.html',
  styleUrl: './console.component.css'
})
export class ConsoleComponent {
  console: boolean = true;
  errors: boolean = false;
  symbols: boolean = false;

  code: string = '';
  errorList: any;

  constructor(private receivedData: SendToServerService) {
    // this.receivedData.variableSubject.subscribe(data => {
    //   this.code = data;
    // });
  }
  setConsole(): void {
    this.console = true;
    this.errors = false;
    this.symbols = false;
  }
  setErrors(): void {
    this.console = false;
    this.errors = true;
    this.symbols = false;
  }
  setSymbols(): void {
    this.console = false;
    this.errors = false;
    this.symbols = true;
  }
  getReceivedData(): any {
    return this.receivedData.object;
  }




}
