import { Injectable } from '@angular/core'
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FlightService {
  private outboundFlights = [];
  private returnFlights = [];
  private isRoundTrip = true;

  constructor() {}

  getOutboundFlights() {
    return of(this.outboundFlights);
  }

  setOutboundFlights(flights) {
    this.outboundFlights = flights;
  }

  getReturnFlights() {
    return of(this.returnFlights)
  }

  setReturnFlights(flights){
    this.returnFlights = flights
  }

  getIsRoundTrip() {
    return this.isRoundTrip;
  }

  setIsRoundTrip(isRoundTrip) {
    this.isRoundTrip = isRoundTrip;
  }
}