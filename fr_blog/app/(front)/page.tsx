import Image from "next/image";

const baseUrl = "http://127.0.0.1:8000";

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
type TImage = {
    id: number;
    meta: {
        type: string;
        detail_url: string;
        download_url: string;
    };
    title: string;
};
type TData = {
    meta: { total_count: number };
    items: {
        id: number;
        meta: TMeta;
        title: string;
        banner_title: string;
        banner_intro: string;
        banner_image: TImage;
    }[];
};

const constructUrl = () => {
    return ``;
};

async function getData(): Promise<TData> {
    const res = await fetch(
        "http://127.0.0.1:8000/api/v2/pages/?slug=home&type=home.HomePage&fields=banner_title,banner_intro,banner_image"
    );
    return res.json();
}

export default async function Page() {
    const data = await getData();
    const page = data.items[0];
    return (
        <div>
            <Image
                src={`${baseUrl}${page.banner_image.meta.download_url}`}
                alt={page.banner_image.title}
                width={1039}
                height={584}
            />
            <h1>{page.banner_title}</h1>
            <p style={{ whiteSpace: "pre" }}>{page.banner_intro}</p>
        </div>
    );
}
