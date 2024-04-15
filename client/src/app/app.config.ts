import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';

import { routes } from './app.routes';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), importProvidersFrom(MonacoEditorModule.forRoot()), provideHttpClient()]
};
