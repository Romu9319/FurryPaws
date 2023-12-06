import React, { useState } from 'react';

export const Jumbotron = () => {

    return (

        <div className="jumbotron jumbotron-fluid px-2 py-5 mt-5" id='jumbotron-home'>
            <div className="container container-jumbotron-home py-3 px-4">
                <div className="p-3 rounded main-light-blue-bg-jumbotron-title">
                    <h1 className="card-title-jumbotron"><strong >All</strong> the services <strong>for your pet</strong> in one place</h1>
                </div>
                <div className="spacer"></div>
                <hr className="my-4"></hr>
                <div className="cards-list-jumbotron-home px-2 py-4">
                    <h6 className="lh-base"> 
                        <span className="main-title" style={{ fontWeight: 'bold' }} >
                            FurryFriends</span> is an online platform designed to unite passionate animal 
                            workes and committed pet owners in a virtual space dedicated to animal care and
                            welfare. <br />Mission: Our mission is to create an online community where vets, 
                            walkers and groomers professionals can offer their expertise and exceptional 
                            services, while pet lovers can find high quality care for their furry companions 
                            and even adopt a new furry friend.
                    </h6>
                </div>
            </div>
        </div>

    );
};