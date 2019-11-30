import { Component, OnInit } from '@angular/core';
import { FlightService } from 'src/service/flight.service';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit {

  outboundFlights = [];
  returnFlights = [];
  isRoundTrip = true;

  constructor(private flightService: FlightService) { }

  ngOnInit() {
    this.flightService.getOutboundFlights().subscribe(flights => this.outboundFlights = flights);
    this.flightService.getReturnFlights().subscribe(flights => this.returnFlights = flights);
    this.isRoundTrip = this.flightService.getIsRoundTrip();
  }

}
