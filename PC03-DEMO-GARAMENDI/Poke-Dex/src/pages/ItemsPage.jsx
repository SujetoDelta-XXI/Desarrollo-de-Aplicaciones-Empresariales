import { useState, useEffect } from "react";
import Favorites from "../components/Favorites";
import Items from "../components/Items";

function HomePage() {
  return (
    <>
      <Favorites />
      <Items />
    </>
  );
}

export default HomePage;
