import { API_PAGES_URL } from "@/common/constants";
import { TGetBlogURL } from "../types";

export function getBlogUrl({ slug, fields }: TGetBlogURL): string {
    if (slug.length === 0) {
        throw new Error("getBlogUrl requires slug");
    }
    return `${API_PAGES_URL}?slug=${slug.trim()}&type=blog.BlogDetailPage&fields=${fields.join()}`;
}
