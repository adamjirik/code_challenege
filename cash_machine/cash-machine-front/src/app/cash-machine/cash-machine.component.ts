import { Component, OnInit } from '@angular/core';
import {CashMachineService} from "../services/cash-machine.service";
import {ToastrService} from "ngx-toastr";

@Component({
  selector: 'app-cash-machine',
  templateUrl: './cash-machine.component.html',
  styleUrls: ['./cash-machine.component.css']
})
export class CashMachineComponent implements OnInit {

  bills: Array<any>;

  constructor(private toastr: ToastrService,
              private cashMachineService: CashMachineService) { }

  ngOnInit() {
  }

  makeWithdrawl(amount: number) {
    this.cashMachineService.withdraw(amount).then(res => {
      this.toastr.success("Withdrawl success");
      this.bills = [];
      this.bills = JSON.parse(res['bill_list']);
    }, res => {
      console.log(res);
      this.toastr.error("Withdrawl failed");
    })
  }

}
