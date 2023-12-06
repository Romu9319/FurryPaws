import React, { useState } from 'react';
import { Link } from 'react-router-dom';


export const UnsignedProfessionalCard = ( { unsignedProfessionals } ) => {
    const [ userId, setUserId ] = useState( localStorage.getItem( "id" ) );
    return (
        <>
            <div className="row d-flex justify-content-center ">
                { unsignedProfessionals !== null && unsignedProfessionals.map( ( professional ) => (
                    <div key={ professional.id } className="card col-md-3 col-lg-3 col-xl-3 m-3 px-0 position-relative" style={{ width: "15rem", height: "14rem" }} >   
                        <h6 className="mb-2 m-2 p-3">
                            <a href="#!.html" className="text-reset">{ professional.title } </a>
                        </h6>
                        <div className="text-center m-2">                            
                            <small className="text-muted" style={ { fontSize: "12px" } } >{ professional.address }</small>
                        </div>
                        <ul className="list-group list-group-flush position-absolute bottom-0 start-0 w-100">
                                { localStorage.getItem( "email" ) &&
                                    <>
                                        <li className="list-group-item px-3 d-flex justify-content-center  project-blue ">
                                            <div className="me-2">
                                                <h6 className="text-whitemt-2">Phone:</h6>
                                            </div>
                                            <div>
                                                <h6 className="">{ professional.phoneNumber }</h6>
                                            </div>
                                        </li>
                                        <li className="list-group-item  d-flex justify-content-center ">
                                            <div>
                                                <a href={ professional.website ? professional.website : '#' } className="btn mt-2" target="blank">Website</a>
                                            </div>
                                        </li>
                                    </>
                                }
                                { !localStorage.getItem( "email" ) && <Link to="/login" class="btn btn-outline-primary project-blue text-white">SignIn To See Contact</Link>
                                }
                            </ul>                            
                    </div>
                ) ) }
                <hr className="mt-3 main-btn" />
            </div>
        </>
    );
};
