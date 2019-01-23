import { Component, OnInit } from '@angular/core';
import {LoginService} from "../services/login.service";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private loginService: LoginService) { }

  ngOnInit() {
  }

  doLogin(username, password) {
    this.loginService.doLogin(username, password).then(res => {
      console.log(res);
      localStorage.setItem('TOKEN', res['token'])
    })
  }
}
