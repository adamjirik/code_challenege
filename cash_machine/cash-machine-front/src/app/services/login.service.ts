import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private BASE_URL = "/api/getToken/";

  constructor(private http: HttpClient) { }

  doLogin(username: string, password:string) {
    return this.http.post(this.BASE_URL, {'username': username, 'password': password}).toPromise()
  }
}
