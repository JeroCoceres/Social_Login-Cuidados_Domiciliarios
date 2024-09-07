import axios from "axios";
import { jwtDecode } from "jwt-decode";
import dayjs from "dayjs";


const token=localStorage.getItem('access') ? JSON.parse(localStorage.getItem('access')) : ""
const refresh_token=localStorage.getItem('refresh') ? JSON.parse(localStorage.getItem('refresh')) : ""

const baseURL="http://localhost:8000/api/v1"
const axiosInstance=axios.create({
    baseURL:baseURL,
    'Content-type':'application/json',
    headers:{'Authorization': localStorage.getItem('access')? `Bearer ${token}` : null}

})

axiosInstance.interceptors.request.use(async req => {
    let token = localStorage.getItem('access') ? JSON.parse(localStorage.getItem('access')) : ""
    req.headers.Authorization = token ? `Bearer ${token}` : null;

    if (token) {
        const user = jwtDecode(token);
        const isExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;

        if (!isExpired) {
            return req;
        } else {
            // El token ha expirado, intenta refrescarlo
            try {
                const refresh_token = JSON.parse(localStorage.getItem('refresh'));
                const res = await axios.post(`${baseURL}/auth/token/refresh/`, { refresh: refresh_token });
                if (res.status === 200) {
                    localStorage.setItem('access', JSON.stringify(res.data.access));
                    req.headers.Authorization = `Bearer ${res.data.access}`;
                    return req;
                }
            } catch (error) {
                console.error("Error al refrescar el token:", error);
                // Opcional: Manejar el logout aquí si el refresh falla
            }
        }
    }

    return req;
});


console.log("axiosInstance : ")


export default axiosInstance