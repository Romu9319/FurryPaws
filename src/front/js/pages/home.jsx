import React from "react";
import { useContext } from "react";
import { Context } from "../store/appContext";
import { Navbar } from "../component/navbar/Navbar.jsx"
import { Jumbotron } from "../component/jumbotron/Jumbotron.jsx";
import { Modal } from "../component/jumbotron/jumbotronComponents/Modal.jsx";


export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<>
			<h1>
				Spain 44 final project
			</h1>
			{/*Navbar */}
			<Navbar />
			{/*END of Navbar */}

			{/*Jumbotron */}
			<Jumbotron />
			<Modal />

			{/*Select Professional*/}

			{/*Footer*/}
		</>
	);
};
