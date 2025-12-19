import { useEffect, useState } from 'react'
import CardList from '../components/CardList'
import getDog from '../services/dog.service'

const Home = ({}) => {
    const { dogs, setDogs } = useState([]);

    useEffect(() => {
        const fetchDog = async () => {
            const dataDog = getDog();
            setDogs(dataDog);
        };
        fetchDog()
    }, [])

    return(
        <section>
            <div>
                <h1>Lista de perros</h1>
                <CardList dogs={dogs}/>
            </div>
        </section>
    )
}

export default Home;