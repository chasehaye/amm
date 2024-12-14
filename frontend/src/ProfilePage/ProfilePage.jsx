import React, { useContext } from 'react';
import { UserContext } from '../UserProvider';

function ProfilePage() {
    const { user } = useContext(UserContext);
    return (
        <>
        <div className='flex flex-col justify-center items-center'>
            <div className="flex justify-center items-center w-full">
                Profile - {user.name} - {user.id} - Dev Notes
            </div>
            ==============
            <div>
                revise the back end to send better info to the backend ((better error handling should be the focus))
            </div>
            -
            <div>
                revise the front to then handle
            </div>
            ==============
            <div>
                fix the user update display margins areminimizing images
            </div>
            -
            <div>
                add anime views for the users since there are none
            </div>
            -
            <div>
                consider pagifying through useffect the indexing of data
            </div>
        </div>
        </>
    )
}

export default ProfilePage;