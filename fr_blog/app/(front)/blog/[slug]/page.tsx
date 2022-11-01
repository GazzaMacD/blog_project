import { getBlogUrl } from "@/common/api_utils/blog_api_utils";
import { TBlogFieldsList } from "@/common/types";
import { API_BASE_URL } from "@/common/constants";
import Image from "next/legacy/image";

type TContentImage = {
    id: number;
    title: string;
    original: {
        src: string;
        width: number;
        height: number;
        alt: string;
    };
};
type TGetBlogDetailResp = {
    meta: {
        total_count: number;
    };
    items: {
        id: number;
        meta: {
            type: string;
            detail_url: string;
            html_url: string | null;
            slug: string;
            first_published_at: string;
        };
        title: string;
        editable_title?: string;
        intro?: string;
        top_image?: {
            id: number;
            meta: {
                type: string;
                detail_url: string;
                download_url: string;
            };
        };
        published_date?: string;
        content?: Array<
            | { type: "text_block"; value: string; id: string }
            | {
                  type: "full_width_image";
                  value: { image: TContentImage; caption: string };
                  id: string;
              }
        >;
    }[];
};

async function getBlogDetail(slug: string) {
    const fields: TBlogFieldsList = [
        "editable_title",
        "intro",
        "content",
        "published_date",
        "top_image",
    ];
    const res = await fetch(getBlogUrl({ slug, fields }));
    return res.json();
}
type TBlogDetailPageProps = {
    params: { slug: string };
};

async function BlogDetailPage({ params }: TBlogDetailPageProps) {
    const { slug } = params;
    const data: TGetBlogDetailResp = await getBlogDetail(slug);
    const blog = data.items[0];
    return (
        <div>
            <h1>{blog.title}</h1>
            <div
                style={{ width: "100%", height: "70vh", position: "relative" }}
            >
                <Image
                    src={`${API_BASE_URL}${blog.top_image?.meta.download_url}`}
                    alt={`Image for ${blog.title}`}
                    layout="fill"
                    objectFit="cover"
                    objectPosition="top"
                />
            </div>
            <div>
                {blog?.content &&
                    blog.content.map((content) => {
                        if (content.type === "text_block") {
                            return (
                                <div
                                    key={content.id}
                                    dangerouslySetInnerHTML={{
                                        __html: content.value,
                                    }}
                                />
                            );
                        }
                        if (content.type === "full_width_image") {
                            const src = `${API_BASE_URL}${content.value.image.original.src}`;
                            console.log(src);
                            return (
                                <div
                                    key={content.id}
                                    style={{
                                        width: "100%",
                                        height: "70vh",
                                        position: "relative",
                                    }}
                                >
                                    <Image
                                        src={src}
                                        alt={content.value.image.original.alt}
                                        layout="fill"
                                        objectFit="cover"
                                        objectPosition="top"
                                    />
                                </div>
                            );
                        }
                    })}
            </div>
        </div>
    );
}

export default BlogDetailPage;
