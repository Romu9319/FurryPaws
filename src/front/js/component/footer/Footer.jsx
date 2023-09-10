import React from 'react'
import { DevelopersComponent } from './footerComponents/DevelopersComponent.jsx'
import { InfographicComponent } from './footerComponents/InfographicComponent.jsx'
import { SocialMediaComponent } from './footerComponents/SocialMediaComponent.jsx'
import { LogoComponent } from './footerComponents/LogoComponent.jsx'

export const Footer = () => {
    return (

        <footer className='footer mt-auto bg-light text-dark'>
            <div className='container text-center text-md-start'>
                <div className='row text-center text-md-start'>
                    {/* Aqui poner el componente con el logo de la web*/}
                    <LogoComponent />
                    <InfographicComponent />
                    <DevelopersComponent />
                    <hr className='mb-2' />
                    <SocialMediaComponent />
                </div>
            </div>
        </footer>
    )
}