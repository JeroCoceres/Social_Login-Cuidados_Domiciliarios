import React, {useState, useEffect, useCallback} from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

const Signup = () => {
    const navigate=useNavigate()
    const[formdata, setFormData]=useState({
        email:"",
        first_name:"",
        last_name:"",
        password:"",
        password2:""
    })

    const handleSignInWithGoogle = async(response)=>{
        const payload=response.credential
        const server_res=await axios.post("http://localhost:8000/api/v1/auth/google/", {"access_token":payload})
        console.log(server_res)
        const user={
            "email":server_res.data.email,
            "names":server_res.data.full_name
        }
        if (server_res.status === 200){
            localStorage.setItem("user", JSON.stringify(user))
            localStorage.setItem("access", JSON.stringify(server_res.data.access_token))
            localStorage.setItem("refresh", JSON.stringify(server_res.data.refresh_token))
            navigate("/dashboard")
            toast.success("login successfull")
        }
    }

    useEffect(()=>{
        google.accounts.id.initialize({
            client_id:import.meta.env.VITE_CLIENT_ID,
            callback:handleSignInWithGoogle
        });
        google.accounts.id.renderButton(
            document.getElementById("signInDiv"),
            {theme:"outline", size:"large", text:"continue_with", shape:"circle", width:"280"}
        )
    },[])


    const [error, setError]=useState("")

    const handleOnChange = (e) => {
        setFormData({...formdata,[e.target.name]:e.target.value})
    }
const {email,first_name,last_name,password,password2}=formdata


    const handleSubmit =  async (e)=>{
        e.preventDefault()
        if (!email || !first_name || !last_name || !password || ! password2) {
            setError("All fields are required")
        }else{
            console.log(formdata)
            const res = await axios.post("http://localhost:8000/api/v1/auth/register/",formdata)
        const response = res.data
        console.log(response)
        if (res.status === 201) {
        navigate("/otp/verify")
        toast.success(response.message)
        }
    }
    }



    return (
        <div>
            <div className="form-container">
                <div style={{width:"100%"}} className="wrapper" >
                    <h2>Create Account</h2>
                    <form onSubmit={handleSubmit}>
                    <p style={{color:"red", padding:"1px"}}>{error ? error : "" }</p>
                    <div>
                        <div className='form-group'>
                            <label htmlFor="">Email Address:</label>
                            <input type="text"
                            className="email-form"
                            name="email"
                            value={email}
                            onChange={handleOnChange}
                            />
                        </div>
                        <div className='form-group'>
                            <label htmlFor="">First Name:</label>
                            <input type="text"
                            className="email-form"
                            name="first_name"
                            value={first_name}
                            onChange={handleOnChange}
                            />
                        </div>
                        <div className='form-group'>
                            <label htmlFor="">Last Name:</label>
                            <input type="text"
                            className="email-form"
                            name="last_name"
                            value={last_name}
                            onChange={handleOnChange}
                            />
                        </div>
                        <div className='form-group'>
                            <label htmlFor="">Password:</label>
                            <input type="password"
                            className="email-form"
                            name="password"
                            value={password}
                            onChange={handleOnChange}
                            />
                        </div>
                        <div className='form-group'>
                            <label htmlFor="">Confirm password:</label>
                            <input type="password"
                            className="email-form"
                            name="password2"
                            value={password2}
                            onChange={handleOnChange}
                            />
                            <input type="submit" value="Submit" className="submitButton"/>
                        </div>
                    </div>
                    </form>
                    <h3 className="text-option">Or</h3>
                    <div className="githubContainer">
                        <button>Sign up with Github</button>
                    </div>
                    <div className="googleContainer" id='signInDiv'>
                        
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Signup