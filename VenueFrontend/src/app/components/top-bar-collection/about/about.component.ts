import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {marked} from "marked"

@Component({
  selector: 'app-about',
  imports: [],
  templateUrl: './about.component.html',
  styleUrl: './about.component.css'
})
export class AboutComponent implements OnInit {
  aboutHtml: string = '';

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('assets/data/about.md', { responseType: 'text' }).subscribe(async markdown => {
      this.aboutHtml = await marked.parse(markdown);
    });
  }
}
