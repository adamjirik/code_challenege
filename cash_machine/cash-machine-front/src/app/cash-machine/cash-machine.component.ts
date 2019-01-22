import { Component, OnInit } from '@angular/core';
import {CashMachineService} from "../cash-machine.service";

@Component({
  selector: 'app-cash-machine',
  templateUrl: './cash-machine.component.html',
  styleUrls: ['./cash-machine.component.css']
})
export class CashMachineComponent implements OnInit {

  constructor(private cashMachineService: CashMachineService) { }

  ngOnInit() {
  }

  makeWithdrawl(amount: number) {
    this.cashMachineService.withdraw(amount).then(res => {
      console.log(res);
    }, res => {
      console.log(res);
    })
  }

}
