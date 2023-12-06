import React from 'react';
import { Link } from 'react-router-dom';


const placeholderImage = "https://img.freepik.com/free-vector/cute-dog-cat-friend-cartoon_138676-2432.jpg?w=2000";

export const PetProfileCard = ( { animal } ) => {


    const { name, breeds, age, description, photos, url } = animal;

    const replaceImage = ( error ) => {
        //replacement of broken Image
        error.target.src = placeholderImage;
    };

    return (
        <>
                <div className="card m-3" style={ { width: "18rem" } }>
                    <img src={ typeof photos[ 0 ] == 'undefined' ? "https://img.freepik.com/free-vector/cute-dog-cat-friend-cartoon_138676-2432.jpg?w=2000" : photos[ 0 ].medium } style={{ width: "100%", height: "18rem" }} />
                    <div className="text-center card-header"  style={{color:"#FE6244"}}>Name: { name } - { breeds.primary }</div>
                    <div className="text-center" style={{ maxHeight: "15rem"}}>
                       <p className='m-2'>{ description }  </p>                       
                    </div>
                    <div className="m-3 mt-1">
                        <Link className="btn" href={ url }  target="blank">Adopt Me</Link>
                    </div>                                     
                </div>
            
        </>
    );
};
