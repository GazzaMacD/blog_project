// API UTILS
export type TBlogFields =
    | "editable_title"
    | "intro"
    | "top_image"
    | "published_date"
    | "content";

export type TBlogFieldsList = TBlogFields[];
export type TGetBlogURL = {
    slug: string;
    fields: TBlogFieldsList;
};
