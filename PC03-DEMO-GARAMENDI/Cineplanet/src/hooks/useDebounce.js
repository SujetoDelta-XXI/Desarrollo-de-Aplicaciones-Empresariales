import { useState, useEffect } from 'react';

function useDebounce(value, delay = 300) {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(timer); // Limpia el temporizador si el valor cambia antes del tiempo
  }, [value, delay]);

  return debouncedValue;
}

export default useDebounce;
