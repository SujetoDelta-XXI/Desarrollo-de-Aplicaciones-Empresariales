import axios from 'axios'

export const getDogs = async () => {
    try {
        const response = await axios.get("https://dog.ceo/api/breed/hound/list");
        return response.data.messaje;

    } catch(error) {
        console.error("Error encontrado");
        return([])
    }
}
