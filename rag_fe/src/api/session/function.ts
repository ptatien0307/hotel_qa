import axios from "axios";

export const getAllSession = async (): Promise<SessionDataType[]> => {
    const response = await axios.get(`/api/apis/session/`);
    const response_data = response.data.data;
    return response_data;
};

export const updateSession = async (
    session_id: string,
    session_new_data: string[]
) => {
    const data = {
        session_id: session_id,
        history: session_new_data,
    };

    const response = await axios.post(`/api/apis/session/${session_id}`, data, {
        headers: {
            "Content-Type": "application/json",
        },
    });
    return response;
};

export const createSession = async (user_id: string) => {
    const data = {
        user_id: user_id,
    };
    const response = await axios.post(`/api/apis/session/`, data, {
        headers: {
            "Content-Type": "application/json",
        },
    });
    return response;
};

export const deleteSession = async (session_id: string) => {
    const response = await axios.delete(`/api/apis/session/${session_id}`);
    return response;
};
