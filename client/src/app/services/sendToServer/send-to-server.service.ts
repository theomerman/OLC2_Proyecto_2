import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SendToServerService {
  // send json to api
  constructor(private http: HttpClient) {
    this.object = {
      "console": "",
      "errors": [],
    };
  }
  object: any;

  sendCode(data: any) {
    // return this.http.post('http://localhost:5000/sendCode', { code: data });
    return this.http.post('http://localhost:5000/sendCode', data, { responseType: 'json' });

  }
  variableSubject = new BehaviorSubject<string>('');

  get variableValue(): string {
    return this.variableSubject.value;
  }

  set variableValue(value: string) {
    this.variableSubject.next(value);
  }
}
