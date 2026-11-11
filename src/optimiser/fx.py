def convert_to_home_currency(r_asset: float, r_fx: float) -> float:
    """Convert a foreign-asset return into the investor's home currency.

    r_fx = return of the foreign currency measured in home-currency units
    """

    return (1 + r_asset) * (1 + r_fx) - 1
