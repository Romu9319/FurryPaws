import React, { useEffect } from "react";

const handleOnErrorImg = ( e ) => {
    e.target.src = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png";
};

export const Avatar = ( { avatar } ) => {
    useEffect( () => {

    }, [ avatar ] );

    return (
        <>
            <div className="rounded float-start">
                <img src={ avatar }
                    alt="profile picture"
                    onError={ handleOnErrorImg }
                    className="w-75 p-3" />
            </div>
        </>
    );
};