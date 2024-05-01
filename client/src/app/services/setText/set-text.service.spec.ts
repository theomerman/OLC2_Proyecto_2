import { TestBed } from '@angular/core/testing';

import { SetTextService } from './set-text.service';

describe('SetTextService', () => {
  let service: SetTextService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SetTextService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
