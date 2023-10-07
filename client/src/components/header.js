export const Header = ({ title }) =>
(
    <>
    
        <div className='w-full h-full object-fill bg-fixed bg-[url("https://www.universityofcalifornia.edu/sites/default/files/styles/article_default_banner/public/Music.Memory.hero_.jpg?itok=AwXJVd9h")]'>
            <div className='flex flex-col justify-center items-center w-full h-full gap-3 backdrop-blur-sm backdrop-brightness-75'>
                <h1 className='lg:text-7xl text-5xl text-white font-bold uppercase transition duration-300 hover:drop-shadow-lg'>{title}</h1>
                <button className="bg-navy-300 px-32 py-5 uppercase rounded-full drop-shadow-lg">
                    <h1 className='lg:text-3xl text-xl text-white font-bold uppercase transition duration-300 hover:drop-shadow-lg'>Generate</h1>
                </button>
            </div>
        </div>
    
    </>
)