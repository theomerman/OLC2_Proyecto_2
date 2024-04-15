import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SetTextService {

  constructor() { }

  private stringSource = new Subject<string>();
  string$ = this.stringSource.asObservable();

  sendString(message: string) {
    this.stringSource.next(message);
  }
}
