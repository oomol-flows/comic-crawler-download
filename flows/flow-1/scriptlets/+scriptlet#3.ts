//#region generated meta
type Inputs = {
    url: string;
    save_dir: string;
};
type Outputs = {
    file_path: string;
};
//#endregion

import type { Context } from "@oomol/types/oocana";
import fs from "fs";
import path from "path";
import fetch from "node-fetch";

export default async function(
    params: Inputs,
    context: Context<Inputs, Outputs>
): Promise<Partial<Outputs> | undefined | void> {
    const { url, save_dir } = params;
    const response = await fetch(url);
    const buffer = await response.buffer();
    const filename = path.basename(url);
    const save_path = path.join(save_dir, filename);
    fs.writeFileSync(save_path, buffer);
    return { save_path };
};