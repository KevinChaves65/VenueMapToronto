import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-about-page',
  imports: [CommonModule],
  templateUrl: './about-page.component.html',
  styleUrl: './about-page.component.css'
})
export class AboutPageComponent implements OnInit {
  aboutHtml: string = '';
  missionHtml: string = '';

  team = [
    { name: 'Kevin Chaves', role: 'Co Founder/Software Developer', LinkedinUrl: "https://www.youtube.com/watch?v=PDJLvF1dUek", img: 'assets/images/team/kevin.jpg' },
    { name: 'Daniel A', role: 'Co Founder/Outreach', LinkedinUrl: "https://www.youtube.com/watch?v=PDJLvF1dUek", img: 'assets/images/team/dan.jpg' },
    { name: 'Adolfo David Romero', role: 'Software Developer', LinkedinUrl: "https://www.youtube.com/watch?v=PDJLvF1dUek", img: 'assets/images/team/david.jpg' },
    { name: 'Evan', role: 'Software Developer', LinkedinUrl: "https://www.youtube.com/watch?v=PDJLvF1dUek", img: 'assets/images/team/evan.jpg' },
    { name: 'Rani', role: 'UI Designer', LinkedinUrl: "https://www.youtube.com/watch?v=PDJLvF1dUek", img: 'assets/images/team/rani.jpg' },
  ];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('assets/data/about.md', { responseType: 'text' }).subscribe(data => this.aboutHtml = data);
    this.http.get('assets/data/mission.md', { responseType: 'text' }).subscribe(data => this.missionHtml = data);
    };
}