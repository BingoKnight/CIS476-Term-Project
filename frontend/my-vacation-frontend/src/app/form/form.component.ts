import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router'
import { FlightService } from '../../service/flight.service'
import * as $ from 'jquery';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  states = [];
  fromCities = [];
  toCities = [];
  errors = [];
  flights = [];

  constructor(private router: Router, private route: ActivatedRoute,
              private flightService: FlightService) { }

  // get list of states in database on intialization
  ngOnInit() {
    $.ajax({
      async: false,
      global: false,
      method: 'GET',
      url: "http://localhost:8000/api/location/getStates",
      success: (data) => {
        this.states = data;
      }
    })

    this.toggleReturnDate()
  }

  tripChange() {
    this.toggleReturnDate()
  }

  // display return date field if round trip is selected, else hide it
  toggleReturnDate() {
    let selected = $('#select-trip option:selected');
    let returnCol = $('#return-date-col');

    if(selected.val() == "RT")
      returnCol.css('display', 'block');
    else
      returnCol.css('display', 'none')
  }

  
  // display cities in based on selected state
  fromStateChanged() {
    this.fromCities = this.getCityList($('#from-state option:selected').val());
  }

  // display cities in based on selected state
  toStateChanged() {
    this.toCities = this.getCityList($('#to-state option:selected').val());
  }

  // pull list of cities queried on the state code
  getCityList(stateCode){
    let temp = null

    $.ajax({
      async: false,
      global: false,
      method: 'GET',
      url: "http://localhost:8000/api/location/getCities/" + stateCode,
      success: (data) => {
        temp =  data;
      }
    })
    return temp;
  }

  // validate that required fields are not empty
  isBlankOrNull(request) {
    let isValidData = false;
    
    if(request.fromCity === '-Select One-'){
      $('#from-city').addClass('error-highlight');
      isValidData = true;
    } else {
      $('#from-city').removeClass('error-highlight');
    }
    
    if(request.fromState === '-Select One-'){
      $('#from-state').addClass('error-highlight');
      isValidData = true;
    } else {
      $('#from-state').removeClass('error-highlight');
    }

    if(!request.depart){
      $('#depart-date').addClass('error-highlight');
      isValidData = true;
    } else {
      $('#depart-date').removeClass('error-highlight');
    }
    
    if(!request.return && request.tripType === 'RT'){
      $('#return-date').addClass('error-highlight');
      isValidData = true;
    } else {
      $('#return-date').removeClass('error-highlight');
    }

    return isValidData;
  }

  // field validation
  isValid(request) {
    let today : Date = new Date();
    let departDate : Date = new Date(request.depart);
    let returnDate : Date = new Date(request.return);
    let isValidData : Boolean = true;

    // increment because takes date minus 1/1/1970, therefore one day behind intended
    departDate.setDate(departDate.getDate() + 1);
    returnDate.setDate(returnDate.getDate() + 1);

    this.errors = [];
    
    if(this.isBlankOrNull(request)){

      this.errors.push('Fill out the highlighted fields');
      isValidData = false;

    } else if(request.fromState === request.toState && 
        (request.fromCity === request.toCity ||
          request.toState === '-Select One-')){
          
      this.errors.push('From and To states and cities cannot match')
      $('#from-state').addClass('error-highlight');
      $('#from-city').addClass('error-highlight');
      $('#to-state').addClass('error-highlight');
      $('#to-city').addClass('error-highlight');

      isValidData = false;
    }

    if(request.tripType === 'RT')
      if(departDate.getTime() < today.getTime() || 
          departDate.getTime() >= returnDate.getTime()){
        this.errors.push('Invalid dates')
        $('#depart-date').addClass('error-highlight');
        $('#return-date').addClass('error-highlight');
        isValidData = false;
      }

    if(isValidData)
      $('#invalid-alert').hide();
    else
      $('#invalid-alert').show();

    return isValidData;
  }

  // validate fields then request flights based on input data
  searchFlights() {

    let toState = $('#to-state option:selected').val() == '-Select One-' ? null : $('#to-state option:selected').val().trim();
    let toCity = $('#to-city option:selected').val() == '-Select One-' ? null : $('#to-city option:selected').text().trim();

    let request = {
      tripType: $('#select-trip option:selected').val(),
      depart: $('#depart-date').val(),
      return: $('#return-date').val() || null,
      fromState: $('#from-state option:selected').val(),
      fromCity: $('#from-city option:selected').text().trim(),
      toState,
      toCity
    }

    if(this.isValid(request)){
      $('#loadingModal').css('display','block');
      this.errors = [];

      $.ajax({
        async: false,
        method: 'POST',
        global: true,
        crossDomain: true,
        data: request,
        url: "http://localhost:8000/api/flight/getFlights",
        success: (data) => {
          this.flightService.setOutboundFlights(data['outbound']);
          this.flightService.setReturnFlights(data['return']);
          this.flightService.setIsRoundTrip(request.tripType == "RT" ? true : false);
        
          $('#loadingModal').css('display','none');
                
          this.router.navigate(['./results'], { relativeTo: this.route });
        }
      })
    }
  }
}