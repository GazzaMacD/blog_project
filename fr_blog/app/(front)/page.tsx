type TMeta = {
    type: string;
    detail_url: string;
    html_url: string | null;
    slug: string;
    show_in_menus: boolean;
    seo_title: string;
    search_description: string;
    first_published_at: string;
    alias_of: string | null;
    locale: string;
};
type TData = {
    meta: { total_count: number };
    items: {
        id: number;
        meta: TMeta;
        title: string;
        banner_title: string;
    }[];
};

async function getData(): Promise<TData> {
    const res = await fetch(
        "http://127.0.0.1:8000/api/v2/pages/?slug=home&type=home.HomePage&fields=banner_title"
    );
    return res.json();
}

export default async function Page() {
    const data = await getData();
    const page = data.items[0];
    return <h1>{page.banner_title}</h1>;
}
