package com.example.prime_numbers_endpoint.api;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PrimeNumbersController {

    /* W celu optymalnego znalezienia rozwiazania konieczne bylo wybranie
    algorytmu o niskiej  zlozonosci obliczeniowej (w tym przypadku N(sqrt(N))
    skorzystano ze strony:
    https://www.scaler.com/topics/prime-Number-between-given-range-in-java/
     */
    public boolean isPrime(long n)
    {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    // mapowanie URI
    @GetMapping("/primes")
    public int getNumbers(@RequestParam("start") int start, @RequestParam("end") int end) {
        int counter = 0;
        for (long i=start; i<=end; i++)
        {
            if (isPrime(i)) {
                counter++;
            }
        }
        return counter;
    }
}
