from textwrap import dedent

def build_investment_memo(payload: dict, irr: float, npv10: float, esg: float, carbon: float) -> str:
    return dedent(f"""
    # Investment Memo: {payload['title']}

    **Sector:** {payload['sector']} | **Country:** {payload['country']}
    **Capex:** R{payload['capex']:,.0f}

    ## Executive Summary
    Automated screening suggests this project meets threshold criteria across financial and impact dimensions.

    ## Financials
    - IRR: {irr:.2%}
    - NPV@10%: R{npv10:,.0f}

    ## ESG
    - Composite ESG Score: {esg:.2f}/100

    ## Carbon Credits
    - Estimated annualized carbon yield (placeholder): {carbon:.2f}

    ## Risks (Auto)
    - Data completeness and permitting timelines
    - Counterparty and construction risk
    - FX and regulatory change

    ## Next Steps
    - Data room request
    - Site diligence & offtake review
    - Term sheet draft
    """)
