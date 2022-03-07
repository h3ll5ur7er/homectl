import { DefaultService } from 'src/app/api';
import { Component } from '@angular/core';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  scripts$ = this.api.listScripts().pipe(map(scripts => scripts || []));
  title = 'homectl';
  results = new Map<string, string>();
  params: {[script: string]: Array<string>} = {
    test42: ['hello', 'world'],
    test13: [],
  }
  constructor(private api: DefaultService) {}
  onRunScript(script:string): void {
    this.api.runScript(script, {params:this.params[script]}).subscribe(result => this.results.set(result.name, result.result));
  }
}
