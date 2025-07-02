//#region generated meta
type Inputs = {
    url: string;
    apikey: string;
};
type Outputs = {
    markdown: string;
};
//#endregion

import type { Context } from "@oomol/types/oocana";
import FirecrawlApp, { ScrapeResponse } from '@mendable/firecrawl-js';

export default async function (
    params: Inputs,
    context: Context<Inputs, Outputs>
): Promise<Partial<Outputs> | undefined | void> {
    const { url, apikey } = params;
    const app = new FirecrawlApp({ apiKey: apikey });

    const scrapeResult = await app.scrapeUrl(url, { formats: ['markdown', 'html'] }) as ScrapeResponse;

    if (!scrapeResult.success) {
        throw new Error(`Failed to scrape: ${scrapeResult.error}`)
    }

    console.log(scrapeResult.markdown)
    context.preview({
        type: "markdown",
        data: scrapeResult.markdown
    })

    return { markdown: scrapeResult.markdown };
};
