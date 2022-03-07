import { ApiModule, DefaultService } from 'src/app/api';
import { BASE_PATH } from './api/variables';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatCardModule } from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ApiModule,
    HttpClientModule,
    MatGridListModule,
    MatCardModule,
  ],
  providers: [
  {provide: BASE_PATH, useValue: window.location.origin+'/api'},
    DefaultService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
