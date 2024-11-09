function Msg({msg}) {
    return (
        <div>
            <p>{msg.user.username}</p>
            <p>{msg.timestamp}</p>
            <p>{msg.body}</p>
        </div>
    );
}

export default Msg;