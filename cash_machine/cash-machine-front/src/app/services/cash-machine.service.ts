import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CashMachineService {

  private BASE_URL = '/api/transactions/';

  constructor(private http: HttpClient,) { }

  withdraw(amount: number) : Promise<any> {
    return this.http.post(this.BASE_URL, {'amount': amount}).toPromise()
  }
}
