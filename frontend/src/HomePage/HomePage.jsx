import { useUser } from "../GlobalProvider"

function Home() {

    const { user } = useUser();

    return(
        <>
        <h1>Home Page</h1>
        {user.loggedInUser ? (
                <p>Welcome, {user.loggedInUser}!</p>
            ) : (
                <p>Please log in to see your personalized content.</p>
            )}
        </>
    )
}

export default Home