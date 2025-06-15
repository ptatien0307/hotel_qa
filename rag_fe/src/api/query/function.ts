import axios from "axios";

export const search = async (query: string) => {
    return await axios.get(`/api/search/${query}`);
};
