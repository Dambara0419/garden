import { useEffect, useState } from "react";

function Display(props){
    const [text, setText] = useState('Loading...')

    useEffect(() => {
        setTimeout(() => {
            setText(`Count: ${props.count}`)
        }, 2000);
    }, [])



    const {count} = props;
    return (
        <div>
            {text}
        </div>
    )
}

export default Display