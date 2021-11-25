const person = {
    firstName : 'shideh',
    lastName: 'parsa',
    birthYear: 1345,
    email: 'shideh@gmail.com',
    hobbies: ['music', 'sports'],
    address: {
      city: 'foo',
      state: 'bar'
    },
    getAge : function(){
      // return 55;
      return 1402 - this.birthYear;
    }
  }
  
  let val;
  
  val = person;
  console.log(val);


  // Get specific value
  val = person.firstName;
  console.log(val);


  val = person['lastName'];
  console.log(val);


  val = person.birthYear;
  console.log(val);

  val = person.hobbies[1];
  console.log(val);


  val = person.address.state;
  console.log(val);


  val = person.address['city'];
  console.log(val);


  val = person.getAge();
  console.log(val);

