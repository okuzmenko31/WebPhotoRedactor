import axios from "axios"

export const fetchToken = async () => {
    try {
        await axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/token/verify/`, { 'token': localStorage.getItem('AuthToken') });
        return true;
    } catch {
        try {
            await setNewToken();
            return true;
        } catch {
            return false;
        }
    }
};

export const setNewToken = () =>{
    return (axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/token/refresh/`, { 'refresh': localStorage.getItem('AuthRefreshToken')})
    .then(res => setLocalToken(res.data.access))
    .catch())
};

//cookie token

export const setTrackingToken = async (token) => {
    return document.cookie = `TrackingToken=${token}`
};

export const getTrackingToken = () => {
    const cookies = document.cookie.split(";").map(cookie => cookie.trim());

    const trackingToken = cookies.find(cookie => cookie.startsWith('TrackingToken='));

    if (trackingToken) {
        return trackingToken.split('=')[1];
    } else {
        return null;
    }
};

export const checkTrackingToken = async () => {
    try {
        const response = await axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/client_ip/`);
        console.log(response);
        return response.data.ip;
    } catch (error) {
        if (getTrackingToken() === null) {
            try {
                const response = await axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/client_token_create/`, {});
                setTrackingToken(response.data.token);
                return getTrackingToken();
            } catch (error) {
                setTrackingToken(error);
                return getTrackingToken();
            }
        } else {
            return getTrackingToken();
        }
    }
}

//Local tokens

export const setLocalToken = async (token) => {
    return localStorage.setItem('AuthToken', token)
};

export const setLocalRefreshToken = async (token) => {
    return localStorage.setItem('AuthRefreshToken', token)
};

export const getLocalToken = () => {
    return localStorage.getItem('AuthToken')
};

export const getLocalRefreshToken = () => {
    return localStorage.getItem('AuthRefreshToken')
};

//headers

export const getHeaders = () => {
    return { 'Authorization': `Bearer ${getLocalToken()}` }
};