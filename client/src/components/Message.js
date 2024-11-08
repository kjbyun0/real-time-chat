function Message({message}) {
    return (
        <div>
            <p>{message.owner.username}</p>
            <p>{message.timestamp}</p>
            <p>{message.body}</p>
        </div>
    );
}

export default Message;