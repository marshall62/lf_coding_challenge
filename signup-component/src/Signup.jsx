import React, {Component} from 'react'
import styles from './Signup.css';

class Signup extends Component {

  constructor(props) {
    super(props);
    this.state = {uname: "", email: "", pw1: "", pw2: "", unameValid: false, emailValid: false,
      pwValid: false, canSubmit: false};
  }

  validateUserName = (e) => {
    const uname = e.target.value.trim();
    this.setState({uname: uname});
    this.setState({unameValid: uname.length <= 15})
  }

  validateEmail = (e) => {
    // validation based on spec ref to:https://stackoverflow.com/questions/2049502/what-characters-are-allowed-in-an-email-address/2049510#2049510
    // and regex ref therein: https://stackoverflow.com/questions/201323/using-a-regular-expression-to-validate-an-email-address
    // Posts in the thread make it clear that the solutions provided are no longer valid.  I've taken the regex
    // from the solution marked correct even though there are posts saying it is inadequate.
    const em = e.target.value.trim().toLowerCase();
    this.setState({email: em});
    const re = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/
    this.setState({emailValid: re.test(em)});

  }

  validate_pws = (pw1, pw2) => {
    this.setState({pwValid: pw1.length > 0 && pw2.length > 0 && pw1 === pw2});
  }

  validate_pw1 = (e) => {
    console.log("pw1 validate");
    this.setState({pw1: e.target.value.trim()});
    this.validate_pws(e.target.value.trim(), this.state.pw2)

  }

  validate_pw2 = (e) => {
    console.log("pw2 validate");
    this.setState({pw2: e.target.value.trim()});
    this.validate_pws(this.state.pw1, e.target.value.trim());
  }

  showUnameErrMsg = () => {
    return this.state.uname.length > 0 && !this.state.unameValid;
  }

  unameValid = () => {
    return this.state.uname.length > 0 && this.state.unameValid;
  }

  showEmailErrMsg = () => {
    return this.state.email.length > 0 && !this.state.emailValid;
  }

  emailValid = () => {
    return this.state.email.length > 0 && this.state.emailValid;
  }

  showPWErrMsg = () => {
    return this.state.pw1.length > 0 && this.state.pw2.length > 0 && !this.state.pwValid;
  }

  pwsValid = () => {
    return this.state.pw1.length > 0 && this.state.pw2.length > 0 && this.state.pwValid;
  }

  // TODO problem.  When typing second password and it matches first,  I can't click submit button
  // because its inactive.  passwords may need onChange handler to update state and validation flag.

  render() {

    let unameMsg = this.showUnameErrMsg() ? "Username cannot be more than 15 chars" : "",
        emailMsg = this.showEmailErrMsg() ? "Email is invalid format" : "",
        pwMsg = this.showPWErrMsg() ? "Passwords do not match" : "",
        allFieldsFilledAndValid = this.unameValid() && this.emailValid() && this.pwsValid();

    return (
        <div className="container Signup-div">

            <label className="Signup-label" htmlFor="username">User Name:</label>

            <span className="Signup-span">{unameMsg}</span>
            <input className="Signup-input" onChange={this.validateUserName} id="username" name="username" type="text" values="{this.state.username}"/>
            <label className="Signup-label" htmlFor="email">Email:</label> <span className="Signup-span">{emailMsg}</span>
            <input className="Signup-input" onBlur={this.validateEmail} id="email" name="email" type="text"/>
            <label className="Signup-label" htmlFor="pw1">Password:</label>
            <input className="Signup-input" onBlur={this.validate_pw1} id="pw1" name="password" type="password"/>
            <label className="Signup-label" htmlFor="pw2">Confirm Password:</label>
            <span className="Signup-span">{pwMsg}</span>
            <input className="Signup-input" onBlur={this.validate_pw2} id="pw2" name="password2" type="password"/>
            <input className="Signup-input" disabled={!allFieldsFilledAndValid} type="submit" value="submit"/>

        </div>);
  }
}

export default Signup;